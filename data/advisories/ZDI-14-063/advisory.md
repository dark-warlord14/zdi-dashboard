# ZDI-14-063: HP Unified Functional Testing ExGrid SaveXML Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-063
- **ZDI-CAN:** ZDI-CAN-1932
- **Date:** 2014-04-08
- **CVE:** CVE-2013-6210
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Unified Functional Testing
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-063/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP Unified Functional Testing. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Exontrol.Grid ActiveX control. The issue lies in the failure to validate the contents of cells before writing them to a file. An attacker can leverage this vulnerability to execute code under the context of the current process.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c04122007

## Disclosure Timeline

- 2013-09-28 - Vulnerability reported to vendor
- 2014-04-08 - Coordinated public release of advisory
