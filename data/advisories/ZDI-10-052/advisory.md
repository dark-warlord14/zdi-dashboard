# ZDI-10-052: Sun Java Runtime Environment XNewPtr Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-052
- **ZDI-CAN:** ZDI-CAN-629
- **Date:** 2010-04-05
- **CVE:** CVE-2010-0843
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Sun Microsystems
- **Affected Products:** Java Runtime
- **Credit:** Peter Vreugdenhil ( http://vreugdenhilresearch.nl )
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-052/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Sun's Java Runtime Environment. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists within a function responsible for allocating objects in the com.sun.media.sound libraries. This function takes an integer parameter and adds a fixed amount to it before allocating from the heap. This can be exploited to gain arbitrary code execution by forcing a call to this allocator with a large enough integer parameter.

## Additional Details

Sun Microsystems has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technology/deploy/security/critical-patch-updates/javacpumar2010.html

## Disclosure Timeline

- 2009-12-10 - Vulnerability reported to vendor
- 2010-04-05 - Coordinated public release of advisory
