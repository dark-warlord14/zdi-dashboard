# ZDI-22-876: Apache HTTPD Server ap_escape_html2 Integer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-22-876
- **ZDI-CAN:** ZDI-CAN-16119
- **Date:** 2022-06-29
- **CVE:** CVE-2022-22721
- **CVSS:** 8.1
- **CVSS Vector:** AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H
- **Affected Vendors:** Apache
- **Affected Products:** HTTPD Server 2.x
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-22-876/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on affected installations of Apache HTTPD Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the ap_escape_html2 function. The issue results from the lack of proper validation of user-supplied data, which can result in an integer overflow before allocating a buffer. An attacker can leverage this vulnerability to execute code in the context of the service account.

## Additional Details

Apache has issued an update to correct this vulnerability. More details can be found at: https://httpd.apache.org/security/vulnerabilities_24.html#CVE-2022-22721

## Disclosure Timeline

- 2021-12-16 - Vulnerability reported to vendor
- 2022-06-29 - Coordinated public release of advisory
