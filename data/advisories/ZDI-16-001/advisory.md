# ZDI-16-001: Unitronics VisiLogic OPLC IDE File Parsing Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-001
- **ZDI-CAN:** ZDI-CAN-2905
- **Date:** 2016-01-06
- **CVE:** CVE-2015-7939
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Unitronics
- **Affected Products:** VisiLogic OPLC IDE
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-001/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Unitronics VisiLogic OPLC IDE. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within parsing of vlp files. A specially crafted vlp will overrun a heap buffer and inject values past the end of the heap allocation. An attacker can leverage this vulnerability to execute arbitrary code under the context of local Administrator.

## Additional Details

Unitronics has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-15-274-02A

## Disclosure Timeline

- 2015-05-01 - Vulnerability reported to vendor
- 2016-01-06 - Coordinated public release of advisory
