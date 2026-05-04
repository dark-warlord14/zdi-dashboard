# ZDI-12-164: (0Day) HP Intelligent Management Center img.exe Integer Wrap Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-164
- **ZDI-CAN:** ZDI-CAN-1389
- **Date:** 2012-08-22
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Intelligent Management Center
- **Credit:** gwslabs.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-164/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett Packard Intelligent Management Center. Authentication is not required to exploit this vulnerability. The specific flaw exists within the img.exe component, which listens by default on TCP port 8800. When handling message packets, the process performs arithmetic on an unvalidated user-supplied values used to determine the size of a new heap buffer, allowing a potential integer wrap to cause a heap buffer overflow. By sending a specially crafted packet, an attacker can leverage this vulnerability to execute code under the context of the user.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 180 day deadline.

## Disclosure Timeline

- 2011-10-21 - Vulnerability reported to vendor
- 2012-08-22 - Coordinated public release of advisory
