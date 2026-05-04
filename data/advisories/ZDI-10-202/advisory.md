# ZDI-10-202: Sun Java Web Start BasicServiceImpl Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-202
- **ZDI-CAN:** ZDI-CAN-705
- **Date:** 2010-10-12
- **CVE:** CVE-2010-3563
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Sun Microsystems
- **Affected Products:** Java Runtime
- **Credit:** Matthias Kaiser (mka)
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-202/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Sun Java Runtime. User interaction is required in that a target must visit a malicious page. The specific flaw exists within the com.sun.jnlp.BasicServiceImpl class. By abusing how Web Start retrieves security policies, an attacker can forge their own and force the removal of sandbox restrictions. Successful exploitation leads to code execution under the context of the user running the browser.

## Additional Details

Sun Microsystems has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpuoct2010-176258.html

## Disclosure Timeline

- 2010-04-05 - Vulnerability reported to vendor
- 2010-10-12 - Coordinated public release of advisory
