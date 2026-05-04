# ZDI-19-1024: Oracle ADF Faces Deserialization of Untrusted Data Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-19-1024
- **ZDI-CAN:** ZDI-CAN-8823
- **Date:** 2019-12-19
- **CVE:** CVE-2019-2904
- **CVSS:** 9.8
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Oracle
- **Affected Products:** ADF Faces
- **Credit:** tint0 of Viettel Cyber Security
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-19-1024/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Oracle ADF Faces. Authentication is not required to exploit this vulnerability. The specific flaw exists within the Remote Regions component. The issue results from the lack of proper validation of user-supplied data, which can result in deserialization of untrusted data. An attacker can leverage this vulnerability to execute code in the context of the web server.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: https://www.oracle.com/security-alerts/cpuoct2019.html

## Disclosure Timeline

- 2019-08-07 - Vulnerability reported to vendor
- 2019-12-19 - Coordinated public release of advisory
- 2021-06-29 - Advisory Updated
