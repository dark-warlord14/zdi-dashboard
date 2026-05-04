# ZDI-17-158: Trend Micro Deep Discovery Email Inspector write_new_html_with_svg Directory Traversal Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-158
- **ZDI-CAN:** ZDI-CAN-4417
- **Date:** 2017-03-09
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Trend Micro
- **Affected Products:** Deep Discovery Email Inspector
- **Credit:** Nikolay Klendar
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-158/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Trend Micro Deep Discovery Email Inspector. Authentication is not required to exploit this vulnerability. The specific flaw exists within write_new_html_with_svg.php. The issue results from the lack of proper validation of a user-supplied path prior to using it in file operations. An attacker can leverage this vulnerability to execute code under the context of root.

## Additional Details

Trend Micro has issued an update to correct this vulnerability. More details can be found at: https://success.trendmicro.com/solution/1116750

## Disclosure Timeline

- 2017-01-05 - Vulnerability reported to vendor
- 2017-03-09 - Coordinated public release of advisory
