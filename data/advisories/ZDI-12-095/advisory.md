# ZDI-12-095: Apple Quicktime TeXML transform Attribute Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-095
- **ZDI-CAN:** ZDI-CAN-1363
- **Date:** 2012-06-21
- **CVE:** CVE-2012-0663
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** QuickTime
- **Credit:** Alexander Gavrun
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-095/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Quicktime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of XML elements within a TeXML file. Specifically, when handling the transform attribute the code within QuickTime3GPP.qtx does not properly validate the length of the data within a translate or matrix object before copying it into a fixed-length buffer on the stack. Exploitation of this vulnerability could allow a remote attacker to execute arbitrary code under the context of the user running Quicktime.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT1222

## Disclosure Timeline

- 2011-10-21 - Vulnerability reported to vendor
- 2012-06-21 - Coordinated public release of advisory
