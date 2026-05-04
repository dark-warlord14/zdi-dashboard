# ZDI-08-043: Sun Java Web Start vm args Stack-Based Buffer Overflow Vulnerability

## Metadata

- **ZDI ID:** ZDI-08-043
- **ZDI-CAN:** ZDI-CAN-287
- **Date:** 2008-07-17
- **CVE:** CVE-2008-3111
- **CVSS:** N/A
- **CVSS Vector:** N/A
- **Affected Vendors:** Sun Microsystems
- **Affected Products:** Java Runtime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-08-043/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Sun Java Web Start. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists in the GetVMArgsOption() function used while parsing the java-vm-args attribute of the j2se tag in xml based JNLP files. When a user downloads a malicious JNLP file, the vulnerable attribute is read into a static buffer. If an overly long value is defined by the java-vm-args attribute, a stack based buffer overflow occurs, resulting in an exploitable condition.

## Additional Details

Sun Microsystems has issued an update to correct this vulnerability. More details can be found at: http://sunsolve.sun.com/search/document.do?assetkey=1-26-238905-1

## Disclosure Timeline

- 2008-01-17 - Vulnerability reported to vendor
- 2008-07-17 - Coordinated public release of advisory
