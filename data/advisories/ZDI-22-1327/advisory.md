# ZDI-22-1327: Apache Batik DefaultScriptSecurity Server-Side Request Forgery Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1327
- **ZDI-CAN:** ZDI-CAN-18356
- **Date:** 2022-10-04
- **CVE:** CVE-2022-40146
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apache
- **Affected Products:** Batik
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1327/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apache Batik. Interaction with this library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the DefaultScriptSecurity class. The issue results from the lack of proper validation of a URI prior to accessing resources. An attacker can leverage this vulnerability to execute code in the context of the current process.

## Additional Details

Apache has issued an update to correct this vulnerability. More details can be found at: https://lists.apache.org/thread/hxtddqjty2sbs12y97c8g7xfh17jzxsx

## Disclosure Timeline

- 2022-08-12 - Vulnerability reported to vendor
- 2022-10-04 - Coordinated public release of advisory
