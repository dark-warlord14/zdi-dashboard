# ZDI-11-014: Red Hat OpenJDK IcedTea6 ClassLoader Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-014
- **ZDI-CAN:** ZDI-CAN-1018
- **Date:** 2011-01-18
- **CVE:** CVE-2010-4351
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:C
- **Affected Vendors:** Red Hat
- **Affected Products:** OpenJDK IcedTea
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-014/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Java OpenJDK. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The flaw exists within the IcedTea.so component. When handling the an applet the process fails to properly restrict permission of code. It is possible to create and instantiate subclasses of ClassLoader. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the browser.

## Additional Details

Red Hat has issued an update to correct this vulnerability. More details can be found at: https://bugzilla.redhat.com/show_bug.cgi?id=CVE-2010-4351

## Disclosure Timeline

- 2010-12-21 - Vulnerability reported to vendor
- 2011-01-18 - Coordinated public release of advisory
