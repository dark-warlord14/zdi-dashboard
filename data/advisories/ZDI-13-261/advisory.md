# ZDI-13-261: HP Virtual User Generator EmulationAdmin Service getReport Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-261
- **ZDI-CAN:** ZDI-CAN-1851
- **Date:** 2013-11-24
- **CVE:** CVE-2013-4839
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Virtual User Generator
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-261/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP Virtual User Generator. Authentication is not required to exploit this vulnerability. The specific flaw exists in the handling of requests to the EmulationAdmin web service. This service exposes the getReport method which does not properly sanitize parameters allowing a remote attacker to inject arbitrary SQL into the underlying database. This can be leveraged by an attacker to gain remote code execution under the context of the current database.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03969437

## Disclosure Timeline

- 2013-04-26 - Vulnerability reported to vendor
- 2013-11-24 - Coordinated public release of advisory
