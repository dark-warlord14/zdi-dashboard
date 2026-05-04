# ZDI-11-199: Oracle Java Soundbank Decompression Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-199
- **ZDI-CAN:** ZDI-CAN-1264
- **Date:** 2011-06-14
- **CVE:** CVE-2011-0802
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Aniway.Anyway@gmail.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-199/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Java parses soundbank files. When a soundbank file contains compressed data it is first decompressed and then Java will parse the decompressed data. Java will read the 'channels' and 'frames' properties from the decompressed data and uses those to calculate a buffer size to store data. An integer wrap can occur during this calculation resulting in the creation of a buffer that is too small to hold all the data. This can result in remote code execution under the context of the current user.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpujune2011-313339.html

## Disclosure Timeline

- 2011-06-02 - Vulnerability reported to vendor
- 2011-06-14 - Coordinated public release of advisory
