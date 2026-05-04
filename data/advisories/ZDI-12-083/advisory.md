# ZDI-12-083: Oracle Java OpenAL Library Pointer Manipulation Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-12-083
- **ZDI-CAN:** ZDI-CAN-1476
- **Date:** 2012-06-06
- **CVE:** N/A
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Chris Ries
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-083/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists in the Java OpenAL (JOAL) library. This library is not installed by default with Java, but it is available as a signed .jar package. The affected jar files are signed with a certificate that is trusted by default JRE installs and as such are downloaded and run without user interaction. Crafted Java applets can reach a call to 'dispatch_alDeleteBuffers1' that takes a user controllable int and uses it as a function pointer. This can lead to remote code execution under the context of the current process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpufeb2012-366318.html

## Disclosure Timeline

- 2011-12-22 - Vulnerability reported to vendor
- 2012-06-06 - Coordinated public release of advisory
