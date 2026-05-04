# ZDI-12-039: Oracle Java Web Start java-vm-args Command Argument Injection Remote Code Execution

## Metadata

- **ZDI ID:** ZDI-12-039
- **ZDI-CAN:** ZDI-CAN-1410
- **Date:** 2012-02-22
- **CVE:** N/A
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-12-039/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the way Java Webstart handles the 'java-vm-args' parameter in the j2se tag within a jnlp file. Due to insufficient sanitation it is possible to add additional double quotes to the commandline argument string used to start a new java process. This can lead to remote code execution under the rights of the current user.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/javacpufeb2012-366318.html

## Disclosure Timeline

- 2011-11-21 - Vulnerability reported to vendor
- 2012-02-22 - Coordinated public release of advisory
