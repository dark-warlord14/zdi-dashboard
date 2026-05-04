# ZDI-16-634: Fatek Automation FvDesigner Stack Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-634
- **ZDI-CAN:** ZDI-CAN-3676
- **Date:** 2016-12-14
- **CVE:** CVE-2016-5798
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Fatek Automation
- **Affected Products:** FvDesigner
- **Credit:** Ariele Caltabiano (kimiya)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-634/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Fatek Automation FvDesigner. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of a FPJ file. A stack-based buffer overflow vulnerability can be triggered in a copy loop while processing a malformed FPJ file. An attacker can leverage this vulnerability to execute arbitrary code in the context of the process.

## Additional Details

Fatek Automation has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-16-287-06

## Disclosure Timeline

- 2016-04-26 - Vulnerability reported to vendor
- 2016-12-14 - Coordinated public release of advisory
