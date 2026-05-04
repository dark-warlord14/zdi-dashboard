# ZDI-08-031: Trillian MSN MIME Header Stack-Based Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-031
- **ZDI-CAN:** ZDI-CAN-323
- **Date:** 2008-05-21
- **CVE:** CVE-2008-2409
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Cerulean Studios
- **Affected Products:** Trillian
- **Credit:** tw33k and n8
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-031/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Cerulean Studios Trillian Pro. Authentication is not required to exploit this vulnerability. The specific flaw exists within the header parsing code for the msn protocol. When processing the X-MMS-IM-FORMAT header, certain attributes are copied into a buffer located on the stack without any length verification which can eventually lead to code execution with the privileges of the user that is running the application.

## Additional Details

Trillian v3.1.10.0 has been released to address these vulnerabilities and is available at http://www.ceruleanstudios.com/downloads/

## Disclosure Timeline

- 2008-05-05 - Vulnerability reported to vendor
- 2008-05-21 - Coordinated public release of advisory
