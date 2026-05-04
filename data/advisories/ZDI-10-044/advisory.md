# ZDI-10-044: Apple QuickTime FLI LinePacket Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-044
- **ZDI-CAN:** ZDI-CAN-601
- **Date:** 2010-04-02
- **CVE:** CVE-2010-0520
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Moritz Jodeit of n.runs AG Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-044/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within QuickTimeAuthoring.qtx during the parsing of DELTA_FLI chunks stored within a malformed .fli file. The applications trusts a user-supplied length for decompression which can be modified to copy more data than necessary leading to a buffer overflow. Successful exploitation can lead to code execution under the context of the current user.

## Additional Details

http://support.apple.com/kb/HT4104 http://support.apple.com/kb/HT4070

## Disclosure Timeline

- 2009-11-06 - Vulnerability reported to vendor
- 2010-04-02 - Coordinated public release of advisory
