# ZDI-12-053: RealNetworks RealPlayer RV30 Sample Arbitrary Index Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-053
- **ZDI-CAN:** ZDI-CAN-1284
- **Date:** 2012-03-26
- **CVE:** CVE-2011-4249
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** RealNetworks
- **Affected Products:** RealPlayer
- **Credit:** Damian Put
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-053/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of RealNetworks Real Player. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within how the application parses sample data encoded with the RV30 codec. When processing certain values within the sample data, the application will use a one as a size for an allocation, and then the use the immediately following byte as an index into that buffer. Due to the lack of correlation between the allocation and the loop that writes to the allocation, this can be used to write outside the buffer and can lead to code execution under the context of the application.

## Additional Details

RealNetworks has issued an update to correct this vulnerability. More details can be found at: http://service.real.com/realplayer/security/11182011_player/en/

## Disclosure Timeline

- 2011-08-12 - Vulnerability reported to vendor
- 2012-03-26 - Coordinated public release of advisory
