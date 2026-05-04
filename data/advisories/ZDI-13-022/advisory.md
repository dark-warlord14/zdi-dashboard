# ZDI-13-022: Oracle Java AWT Image Transform Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-022
- **ZDI-CAN:** ZDI-CAN-1580
- **Date:** 2013-02-11
- **CVE:** CVE-2013-1480
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Chris Ries
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-022/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the Java AWT Image Transform library functions. For certain image transformation functions, Java fails to take the 'numBands' into account during the allocation of heap memory and instead uses a static value of 0x4. The allocated memory is later written to inside a loop that uses the 'numBands' value which can result in a memory corruption. This can lead to remote code execution under the context of the current process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpufeb2013-1841061.html

## Disclosure Timeline

- 2012-10-29 - Vulnerability reported to vendor
- 2013-02-11 - Coordinated public release of advisory
