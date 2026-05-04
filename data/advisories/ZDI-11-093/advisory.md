# ZDI-11-093: CA Internet Security Suite HIPS XML Security Database Parser Class Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-093
- **ZDI-CAN:** ZDI-CAN-882
- **Date:** 2011-02-23
- **CVE:** CVE-2011-1036
- **CVSS:** 9.3
- **CVSS Vector:** AV:N/AC:M/Au:N/C:C/I:C/A:C
- **Affected Vendors:** CA
- **Affected Products:** Internet Security Suite
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-093/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of CA Internet Security Suite 2010. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The flaw exists within the XMLSecDB ActiveX control which is installed with HIPSEngine component. SetXml and Save methods are implemented insecurely and can allow creation of an arbitrary file on the victim's system. A remote attacker can exploit this vulnerability to execute arbitrary code under the context of the user.

## Additional Details

CA has issued an update to correct this vulnerability. More details can be found at: https://support.ca.com/irj/portal/anonymous/phpsupcontent?contentID={53A608DF-BFDB-4AB3-A98F-E4BB6BC7A2F4}

## Disclosure Timeline

- 2010-08-25 - Vulnerability reported to vendor
- 2011-02-23 - Coordinated public release of advisory
