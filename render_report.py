"""Run the existing checks and render their recorded results as a local report."""
import subprocess
import sys
from pathlib import Path
from datetime import datetime, timezone
from html import escape
import xml.etree.ElementTree as ET


def main():
    root=Path(__file__).resolve().parent
    out=root/'build';out.mkdir(exist_ok=True)
    result=subprocess.run([sys.executable,'-m','pytest','tests','-q','--junitxml='+str(out/'results.xml')],cwd=root)
    if not (out/'results.xml').exists():return result.returncode or 1
    cases=ET.parse(out/'results.xml').findall('.//testcase')
    rows=[];passed=failed=skipped=0
    names={'test_row_count':'Matching row counts','test_no_null_customer_id':'Required customer IDs','test_no_duplicate_order_id':'Unique order IDs','test_country_values':'Allowed country names','test_sales_amount_positive':'Positive sales amounts','test_date_format':'Date separator present'}
    for case in cases:
        bad=case.find('failure') is not None or case.find('error') is not None
        skip=case.find('skipped') is not None
        status='FAIL' if bad else 'SKIP' if skip else 'PASS'
        failed+=bad;skipped+=skip;passed+=not bad and not skip
        rows.append('<tr><td class="'+status.lower()+'">'+status+'</td><td>'+escape(names.get(case.get('name'),case.get('name','')))+ '</td><td>'+escape(case.get('classname',''))+'</td><td>'+escape(case.get('time','0'))+' s</td></tr>')
    stamp=datetime.now(timezone.utc).strftime('%d %b %Y %H:%M UTC')
    html="""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Data transfer checks</title><style>*{box-sizing:border-box}body{margin:0;background:#0f1418;color:#dbe4e9;font:15px/1.65 Consolas,monospace}.shell{max-width:1200px;margin:45px auto;border:1px solid #35434c;border-radius:9px;overflow:hidden}.bar{background:#202a31;padding:14px 28px;color:#a9b9c4;font-size:12px;border-bottom:1px solid #35434c}main{padding:35px 38px}small{color:#86a69b;font-size:12px}h1{font:500 42px/1.2 Consolas,monospace;letter-spacing:-2px;margin:15px 0}p{color:#a9b9c4;max-width:850px}.command{border-left:3px solid #6bdbb0;background:#17231f;padding:17px 20px;color:#a4eccf;margin:28px 0}.result{display:flex;gap:45px;padding:18px 0 26px;border-bottom:1px solid #35434c}.result strong{font-size:34px;color:#6bdbb0}.result span{font-size:12px;display:block;color:#a9b9c4}.scroll{overflow:auto}table{width:100%;border-collapse:collapse;font-size:13px;margin:22px 0}td,th{text-align:left;padding:15px 10px;border-bottom:1px solid #2c3941;white-space:nowrap}th{font-size:10px;color:#8d9da7;text-transform:uppercase;letter-spacing:2px}.pass{color:#6bdbb0}.fail{color:#ff9292}.skip{color:#edcb7a}.limits{border-top:1px solid #35434c;padding-top:18px;font-size:12px}.limits b{color:#dbe4e9}footer{padding:16px 28px;background:#202a31;color:#a9b9c4;font-size:11px}@media(max-width:700px){.shell{margin:16px}.bar,main{padding:20px}h1{font-size:30px}.result{gap:24px}.result strong{font-size:26px}}</style></head><body><div class="shell"><div class="bar">LOCAL TEST RUN / DATA VALIDATION</div><main><small>source_system_a.csv → target_system_b.csv</small><h1>Data transfer checks</h1><p>Six basic checks before the destination file is used for reporting.</p><div class="command">$ python -m pytest tests -q</div><div class="result"><div><strong>PASSED</strong><span>passed</span></div><div><strong>FAILED</strong><span>failed</span></div><div><strong>SKIPPED</strong><span>skipped</span></div></div><div class="scroll"><table><thead><tr><th>Result</th><th>Check</th><th>Test module</th><th>Time</th></tr></thead><tbody>ROWS</tbody></table></div><p class="limits"><b>Scope:</b> A passing run does not prove every value transferred correctly. The date check only looks for a dash; it does not validate complete dates. These tests use sample files.</p></main><footer>Recorded STAMP · Python VERSION · Results read from pytest JUnit XML</footer></div></body></html>"""
    for key,value in [('PASSED',str(passed)),('FAILED',str(failed)),('SKIPPED',str(skipped)),('ROWS',''.join(rows)),('STAMP',stamp),('VERSION',sys.version.split()[0])]:html=html.replace(key,value)
    (out/'index.html').write_text(html,encoding='utf-8')
    return result.returncode

if __name__=='__main__':raise SystemExit(main())
