# ZDI-09-077: Sun Java Web Start Arbitrary Command Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-09-077
- **ZDI-CAN:** ZDI-CAN-505
- **Date:** 2009-11-04
- **CVE:** CVE-2009-3866
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Sun Microsystems
- **Affected Products:** Java Runtime
- **Credit:** Peter Csepely
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-09-077/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Sun Java WebStart. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists in the implementation of security model permissions during the removal of installer extensions. By modifying an existing installer extension JNLP file, a condition occurs that allows for code supplied by a different URL than the original installer extension URL to run as a secure applet. This condition can result in arbitrary command injection under the privileges of the currently logged in user.

## Additional Details

Sun Microsystems has issued an update to correct this vulnerability. More details can be found at: http://sunsolve.sun.com/search/document.do?assetkey=1-66-269870-1

## Disclosure Timeline

- 2009-08-17 - Vulnerability reported to vendor
- 2009-11-04 - Coordinated public release of advisory
