# ZDI-22-1328: Apache Batik DefaultExternalResourceSecurity Server-Side Request Forgery Information Disclosure Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-1328
- **ZDI-CAN:** ZDI-CAN-18357
- **Date:** 2022-10-04
- **CVE:** CVE-2022-38398
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N
- **Affected Vendors:** Apache
- **Affected Products:** Batik
- **Credit:** Piotr Bazydlo (@chudypb) of Trend Micro Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-1328/
## Vulnerability Details

This vulnerability allows remote attackers to disclose sensitive information on affected installations of Apache Batik. Interaction with this library is required to exploit this vulnerability but attack vectors may vary depending on the implementation. The specific flaw exists within the DefaultExternalResourceSecurity class. The issue results from the lack of proper validation of a URI prior to accessing resources. An attacker can leverage this vulnerability to disclose information in the context of the current process.

## Additional Details

Apache has issued an update to correct this vulnerability. More details can be found at: https://lists.apache.org/thread/712c9xwtmyghyokzrm2ml6sps4xlmbsx

## Disclosure Timeline

- 2022-08-12 - Vulnerability reported to vendor
- 2022-10-04 - Coordinated public release of advisory
