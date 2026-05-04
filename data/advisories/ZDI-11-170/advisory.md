# ZDI-11-170: (0Day) HP 3COM/H3C Intelligent Management Center img recv Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-170
- **ZDI-CAN:** ZDI-CAN-1019
- **Date:** 2011-05-31
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** H3C Intelligent Management Center
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-170/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP 3COM/H3C Intelligent Management Center. Authentication is not required to exploit this vulnerability. The flaw exists within the img.exe component which listens by default on TCP port 8800. When handling the a packet type the process uses a user provided length value in an arithmetic operation resulting in integer wrapping. The process then copies user supplied data into a fixed-length buffer on the heap. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the SYSTEM user.

## Additional Details

[May 31, 2011] - This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 180 day deadline. -- Mitigation: As the affected component is the 'core' process for IMC, we recommend either disabling this service entirely until a vendor patch is available or denying incoming connections to 8800/tcp, this is the remote vector into the vulnerable code.

## Disclosure Timeline

- 2010-12-01 - Vulnerability reported to vendor
- 2011-05-31 - Coordinated public release of advisory
