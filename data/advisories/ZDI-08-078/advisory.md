# ZDI-08-078: Trillian IMG SRC ID Memory Corruption Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-078
- **ZDI-CAN:** ZDI-CAN-409
- **Date:** 2008-12-04
- **CVE:** CVE-2008-5402
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Trillian
- **Affected Products:** Trillian Pro
- **Credit:** Damian Put
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-078/
## Vulnerability Details

This vulnerability allows remote attackers to potentially execute arbitrary code on vulnerable installations of Cerulean Studios Trillian. Authentication is not required to exploit this vulnerability. The specific flaw exists within the XML processing code for Trillian. When parsing specially formulated xml, the application will corrupt an internal data structure. Whilst deallocating this data structure, the application can be tricked into freeing a single allocated chunk multiple times, which can potentially lead to code execution.

## Additional Details

Trillian has issued an update to correct this vulnerability. More details can be found at: http://blog.ceruleanstudios.com/?p=404

## Disclosure Timeline

- 2008-11-10 - Vulnerability reported to vendor
- 2008-12-04 - Coordinated public release of advisory
