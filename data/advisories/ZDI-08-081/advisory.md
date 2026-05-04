# ZDI-08-081: Sun Java Web Start and Applet Multiple Sandbox Bypass Vulnerabilities

## Metadata

- **ZDI ID:** ZDI-08-081
- **ZDI-CAN:** ZDI-CAN-363
- **Date:** 2008-12-04
- **CVE:** CVE-2008-5339
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Sun Microsystems
- **Affected Products:** Java Runtime
- **Credit:** Peter Csepely
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-081/
## Vulnerability Details

These vulnerabilities allow remote attackers to bypass sandbox restrictions on vulnerable installations of Sun Java Web Start. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The first vulnerability results in a cache location and a user name information disclosure. By accessing the SI_FILEDIR property of a SingleInstanceImpl class, the location of the temporary single instance files can be parsed to discover the user name and cache location. The second vulnerability allows applets to read any file on a victim's filesystem, outside of the restricted path of the applet. The specific flaw exists in the handling of the file: protocol assigned to an applet codebase. If the codebase points to the local filesystem, any file is then readable by the malicious applet. The third vulnerability allows JNLP files to bypass socket restrictions. By loading a secondary JNLP with an href attribute containing a wildcard. When this object is instantiated, all hosts are eligible for socket connect and accept.

## Additional Details

Sun Microsystems has issued an update to correct this vulnerability. More details can be found at: http://sunsolve.sun.com/search/document.do?assetkey=1-66-244988-1

## Disclosure Timeline

- 2008-07-14 - Vulnerability reported to vendor
- 2008-12-04 - Coordinated public release of advisory
