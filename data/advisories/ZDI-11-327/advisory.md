# ZDI-11-327: HP Data Protector Notebook Extension Policy Server LogBackupLocationStatus Remote SQL Injection Vulnerabilty

## Metadata

- **ZDI ID:** ZDI-11-327
- **ZDI-CAN:** ZDI-CAN-1229
- **Date:** 2011-11-07
- **CVE:** CVE-2011-3161
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Data Protector
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-327/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP Data Protector Notebook Extension. Authentication is not required to exploit this vulnerability. The flaw exists within the dpnepolicyservice component which exposes a DPNECentral Web Service on TCP port 80. This service contains a method LogBackupLocationStatus which does not properly validate or sanitize the backupLocationStatus field of a user supplied request. This value is later used when constructing a query fulfill provided request. A remote attacker can exploit this vulnerability to execute arbitrary queries under the context of the service.

## Additional Details

Hewlett-Packard has issued an update to correct this vulnerability. More details can be found at: https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_na-c03058866

## Disclosure Timeline

- 2011-06-03 - Vulnerability reported to vendor
- 2011-11-07 - Coordinated public release of advisory
