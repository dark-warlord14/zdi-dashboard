# ZDI-16-505: AlienVault Unified Security Management get_directive_kdb directive_id SQL Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-16-505
- **ZDI-CAN:** ZDI-CAN-3742
- **Date:** 2016-09-08
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** AlienVault
- **Affected Products:** Unified Security Management
- **Credit:** Peter Lapp
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-16-505/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of AlienVault Unified Security Management. Authentication is not required to exploit this vulnerability. The specific flaw exists when handling get_directive_kdb.php requests. The vulnerability is caused by the lack of input validation on 'directive_id' before using remotely supplied strings to construct SQL queries. An unauthenticated remote attacker can leverage this vulnerability to execute arbitrary code in the context of root.

## Additional Details

AlienVault has issued an update to correct this vulnerability. More details can be found at: https://www.alienvault.com/forums/discussion/7110/

## Disclosure Timeline

- 2016-05-09 - Vulnerability reported to vendor
- 2016-09-08 - Coordinated public release of advisory
