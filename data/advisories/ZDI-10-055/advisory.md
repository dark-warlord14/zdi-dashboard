# ZDI-10-055: Sun Java Runtime Environment Mutable InetAddress Socket Policy Violation Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-055
- **ZDI-CAN:** ZDI-CAN-603
- **Date:** 2010-04-05
- **CVE:** CVE-2010-0095
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Sun Microsystems
- **Affected Products:** Java Runtime
- **Credit:** Sami Koivu
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-055/
## Vulnerability Details

This vulnerability allows remote attackers to violate security policies on vulnerable installations of Sun Java Runtime. User interaction is required to exploit this vulnerability in that the target must run a malicious applet. The specific flaw allows malicious applets to connect to network addresses other than the originating applet and client IPs. A handcrafted applet can override compile time checks to prevent compilation of a mutable InetAddress subclass. This results in the ability to circumvent the Applet SecurityManager restictions.

## Additional Details

Sun Microsystems has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technology/deploy/security/critical-patch-updates/javacpumar2010.html

## Disclosure Timeline

- 2009-10-21 - Vulnerability reported to vendor
- 2010-04-05 - Coordinated public release of advisory
