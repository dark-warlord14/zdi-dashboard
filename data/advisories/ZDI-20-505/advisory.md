# ZDI-20-505: Oracle Business Intelligence AMF Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-20-505
- **ZDI-CAN:** ZDI-CAN-9334
- **Date:** 2020-04-16
- **CVE:** CVE-2020-2950
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** Business Intelligence
- **Credit:** GreenDog
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-20-505/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Oracle Business Intelligence. Authentication is not required to exploit this vulnerability. The specific flaw exists within BIRemotingServlet. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuapr2020.html

## Disclosure Timeline

- 2020-02-26 - Vulnerability reported to vendor
- 2020-04-16 - Coordinated public release of advisory
