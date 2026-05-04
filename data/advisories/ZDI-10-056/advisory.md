# ZDI-10-056: Sun Java Runtime Environment Trusted Methods Chaining Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-056
- **ZDI-CAN:** ZDI-CAN-623
- **Date:** 2010-04-05
- **CVE:** CVE-2010-0840
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Java Runtime
- **Credit:** Sami Koivu
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-056/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Sun Java Runtime. Authentication is not required to exploit this vulnerability. The specific flaw exists within the code responsible for ensuring proper privileged execution of methods. If an untrusted method in an applet attempts to call a method that requires privileges, Java will walk the call stack and for each entry verify that the method called is defined within a class that has that privilege. However, this does not take into account an untrusted object that has extended the trusted class without overwriting the target method. Additionally, this can be bypassed by abusing a similar trust issue with interfaces. An attacker can leverage these insecurities to execute vulnerable code under the context of the user invoking the JRE.

## Disclosure Timeline

- 2009-11-24 - Vulnerability reported to vendor
- 2010-04-05 - Coordinated public release of advisory
