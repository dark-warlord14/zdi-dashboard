# ZDI-13-142: Oracle Java Image ColorConvert Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-13-142
- **ZDI-CAN:** ZDI-CAN-1741
- **Date:** 2013-06-27
- **CVE:** CVE-2013-1493
- **CVSS:** 6.8
- **CVSS Vector:** AV:N/AC:M/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-13-142/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Oracle Java Runtime Environment. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the native code for initImageLayouts. Buffer overflows exist such that a remote attacker can create a custom image class that can leverage these vulnerabilities to execute code under the context of the user running the process.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technetwork/topics/security/alert-cve-2013-1493-1915081.html

## Disclosure Timeline

- 2013-02-22 - Vulnerability reported to vendor
- 2013-06-27 - Coordinated public release of advisory
