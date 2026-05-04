# ZDI-08-042: Sun Java Web Start Sandbox Bypass Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-042
- **ZDI-CAN:** ZDI-CAN-315
- **Date:** 2008-07-17
- **CVE:** CVE-2008-3112
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Sun Microsystems
- **Affected Products:** Java Runtime
- **Credit:** Peter Csepely
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-042/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Sun Java Web Start. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists in the writeManifest() method of the CacheEntry class. A directory traversal flaw in this method allows the creation of arbitrary files on the target system. After the file has been created, a call to Runtime.getRuntime.exec() can be used to execute the file.

## Additional Details

Sun Microsystems has issued an update to correct this vulnerability. More details can be found at: http://sunsolve.sun.com/search/document.do?assetkey=1-26-238905-1

## Disclosure Timeline

- 2008-05-05 - Vulnerability reported to vendor
- 2008-07-17 - Coordinated public release of advisory
