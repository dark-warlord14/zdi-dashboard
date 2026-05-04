# ZDI-12-109: Apple Quicktime TeXML Karaoke Element Parsing Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-109
- **ZDI-CAN:** ZDI-CAN-1367
- **Date:** 2012-06-28
- **CVE:** CVE-2012-0663
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Apple
- **Affected Products:** QuickTime
- **Credit:** Alexander Gavrun
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-109/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Apple Quicktime. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the parsing of XML elements within a TeXML file. Specifically, when handling the karaoke XML element the code within QuickTime3GPP.qtx does not properly validate the length of the data within specific sub-fields. By providing specially crafted data, the code can be made to copy too much data into a fixed-length buffer on the stack. Exploitation of this vulnerability could allow a remote attacker to execute arbitrary code under the context of the user running Quicktime.

## Disclosure Timeline

- 2011-11-04 - Vulnerability reported to vendor
- 2012-06-28 - Coordinated public release of advisory
