# ZDI-17-291: ThinPrint TPView JPEG2000 Parsing Out-Of-Bounds Write Privilege Escalation Vulnerability

## Metadata

- **ZDI ID:** ZDI-17-291
- **ZDI-CAN:** ZDI-CAN-4206
- **Date:** 2017-04-19
- **CVE:** CVE-2017-4911
- **CVSS:** 6.2
- **CVSS Vector:** AV:L/AC:H/Au:N/C:C/I:C/A:C
- **Affected Vendors:** ThinPrint
- **Affected Products:** ThinPrint
- **Credit:** Ke Liu of Tencent's Xuanwu LAB
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-17-291/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of ThinPrint. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within JPEG2000 parsing. The process does not properly validate user-supplied data which can result in a write past the end of an allocated object. An attacker can leverage this vulnerability to execute code under the context of the host OS.

## Additional Details

ThinPrint has issued an update to correct this vulnerability. More details can be found at: https://www.vmware.com/security/advisories/VMSA-2017-0008.html

## Disclosure Timeline

- 2016-11-30 - Vulnerability reported to vendor
- 2017-04-19 - Coordinated public release of advisory
