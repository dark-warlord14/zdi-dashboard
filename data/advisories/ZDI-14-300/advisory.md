# ZDI-14-300: Attachmate AppManager Client Resource Monitor Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-300
- **ZDI-CAN:** ZDI-CAN-2139
- **Date:** 2014-09-03
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Attachmate
- **Affected Products:** AppManager
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-300/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of NetIQ AppManager Client Resource Monitor. Authentication is not required to exploit this vulnerability. The specific flaw exists because the installer defaults to a vulnerable configuration wherein "knowledge script" information is accepted from any source. An attacker can exploit this condition to achieve remote code execution as SYSTEM.

## Additional Details

Attachmate has issued an update to correct this vulnerability. More details can be found at: https://www.netiq.com/support/kb/doc.php?id=7015459&path=725&number=f.1

## Disclosure Timeline

- 2014-05-05 - Vulnerability reported to vendor
- 2014-09-03 - Coordinated public release of advisory
