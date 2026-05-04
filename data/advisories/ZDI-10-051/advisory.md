# ZDI-10-051: Sun Java Runtime RMIConnectionImpl Privileged Context Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-051
- **ZDI-CAN:** ZDI-CAN-588
- **Date:** 2010-04-05
- **CVE:** CVE-2010-0094
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Sun Microsystems
- **Affected Products:** Java Runtime
- **Credit:** Sami Koivu
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-051/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of the Sun Java Runtime Environment. User interaction is required to exploit this vulnerability in that the target must visit a malicious website. The specific flaw exists within the deserialization of RMIConnectionImpl objects. Due to a lack of privilege checks during deserialization it is possible to supply privileged code in the ClassLoader of a constructor being deserialized. This allows for a remote attacker to call system level Java functions without proper sandboxing. Exploitation of this can lead to remote system compromise under the context of the currently logged in user.

## Additional Details

Sun Microsystems has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technology/deploy/security/critical-patch-updates/javacpumar2010.html

## Disclosure Timeline

- 2009-10-21 - Vulnerability reported to vendor
- 2010-04-05 - Coordinated public release of advisory
