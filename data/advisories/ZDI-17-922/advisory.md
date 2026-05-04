# ZDI-17-922: ThinPrint TPView JPEG2000 Parsing Out-Of-Bounds Write Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-922
- **ZDI-CAN:** ZDI-CAN-4856
- **Date:** 2017-11-20
- **CVE:** CVE-2017-4935
- **CVSS:** 6.2
- **CVSS Vector:** AV:L/AC:H/Au:N/C:C/I:C/A:C
- **Affected Vendors:** ThinPrint
- **Affected Products:** ThinPrint
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-922/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of ThinPrint. An attacker must first obtain the ability to execute low-privileged code on the guest system in order to exploit this vulnerability. The specific flaw exists within JPEG2000 parsing. The process does not properly validate user-supplied data, which can result in a write past the end of an allocated object. An attacker can leverage this in conjunction with other vulnerabilities to execute code in the context of the host OS.

## Additional Details

ThinPrint has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2017-0018.html

## Disclosure Timeline

- 2017-06-22 - Vulnerability reported to vendor
- 2017-11-20 - Coordinated public release of advisory
