# ZDI-15-355: Oracle Endeca Information Discovery Integrator ETL Server UploadFileContent Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-355
- **ZDI-CAN:** ZDI-CAN-2772
- **Date:** 2015-07-20
- **CVE:** CVE-2015-2602
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/Au:S/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Endeca Tools and Frameworks
- **Credit:** Steven Seeley of Source Incite
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-355/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable instances of Oracle Endeca Information Discovery. Authentication is required to exploit this vulnerability but an authentication bypass is known. The specific flaw exists within the handling of file uploads using UploadFileContent. The issue lies in the failure to sanitize the path of files uploaded, allowing for them to be placed at an attacker controlled location. An attacker can leverage this vulnerability to execute code in the context of the clover server.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/cpujul2015-2367936.html

## Disclosure Timeline

- 2015-02-25 - Vulnerability reported to vendor
- 2015-07-20 - Coordinated public release of advisory
