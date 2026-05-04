# ZDI-18-527: Advantech WebAccess webvrpcs Service viewdll1 strcpy Heap-Based Buffer Overflow Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-18-527
- **ZDI-CAN:** ZDI-CAN-5897
- **Date:** 2018-05-18
- **CVE:** CVE-2018-8845
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Advantech
- **Affected Products:** WebAccess
- **Credit:** Fritz Sands of the Zero Day Initiative
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-18-527/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable instances of Advantech WebAccess. Authentication is not required to exploit this vulnerability. The specific flaw exists within the implementation of the 0x13C80 IOCTL in the BwOpcTool subsystem. When parsing the NamedObject structure, the process does not properly validate the length of user-supplied data prior to copying it to a fixed-length, heap-based buffer. An attacker can leverage this vulnerability to execute code in the context of Administrator.

## Additional Details

Advantech has issued an update to correct this vulnerability. More details can be found at: https://ics-cert.us-cert.gov/advisories/ICSA-18-135-01

## Disclosure Timeline

- 2018-03-23 - Vulnerability reported to vendor
- 2018-05-18 - Coordinated public release of advisory
- 2018-05-18 - Advisory Updated
