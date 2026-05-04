# ZDI-14-100: Hewlett-Packard Virtual User Generator EmulationAdmin Service Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-100
- **ZDI-CAN:** ZDI-CAN-1833
- **Date:** 2014-04-17
- **CVE:** CVE-2013-6213
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Virtual User Generator
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-100/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP Virtual User Generator. Authentication is not required to exploit this vulnerability. The specific flaw exists within the exposed EmulationAdminSoapBinding web service. The issue lies in the handling of several methods resulting in the ability to read, write, and delete arbitrary files. An attacker can leverage this vulnerability to leak credential databases or execute code under the context of SYSTEM.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03969437

## Disclosure Timeline

- 2014-01-06 - Vulnerability reported to vendor
- 2014-04-17 - Coordinated public release of advisory
