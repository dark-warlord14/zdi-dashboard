# ZDI-13-080: Apple QuickTime MP3 Memory Corruption Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-080
- **ZDI-CAN:** ZDI-CAN-1724
- **Date:** 2013-05-29
- **CVE:** CVE-2103-0989
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** QuickTime
- **Credit:** G. Geshev
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-080/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple QuickTime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the CoreAudioToolbox component processing an mp3 file. Altering the channel_mode value from stereo to mono in the header of a stereo mpeg frame could result in a heap buffer overflow. An attacker could leverage this to gain remote code execution under the context of the process.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT1222

## Disclosure Timeline

- 2013-01-08 - Vulnerability reported to vendor
- 2013-05-29 - Coordinated public release of advisory
