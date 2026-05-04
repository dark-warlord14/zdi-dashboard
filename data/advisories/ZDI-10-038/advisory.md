# ZDI-10-038: Apple QuickTime QDMC/QDM2 Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-038
- **ZDI-CAN:** ZDI-CAN-534
- **Date:** 2010-04-02
- **CVE:** CVE-2010-0060
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** Quicktime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-038/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists in the QuickTimeAudioSupport.qtx library when parsing malformed QDMC and QDM2 codec atoms. By modifying specific values within the stream an attacker can cause heap corruption which can lead to arbitrary code execution under the context of the currently logged in user.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4077

## Disclosure Timeline

- 2009-09-22 - Vulnerability reported to vendor
- 2010-04-02 - Coordinated public release of advisory
