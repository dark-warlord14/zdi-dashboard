# ZDI-13-259: HP Virtual User Generator EmulationAdmin Service copyFileToServer Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-259
- **ZDI-CAN:** ZDI-CAN-1832
- **Date:** 2013-11-24
- **CVE:** CVE-2013-4837
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Virtual User Generator
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-259/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP Virtual User Generator. Authentication is not required to exploit this vulnerability. The specific flaw exists in the handling of requests to the EmulationAdmin web service. This service exposes the copyFileToServer method which contains a directory traversal flaw that allows attackers to create files at arbitrary locations with attacker controlled data. This can be leveraged by an attacker to gain remote code execution under the context of SYSTEM.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03969437

## Disclosure Timeline

- 2013-04-26 - Vulnerability reported to vendor
- 2013-11-24 - Coordinated public release of advisory
