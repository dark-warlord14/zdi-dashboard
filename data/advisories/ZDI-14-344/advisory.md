# ZDI-14-344: (0Day) Hewlett-Packard Data Protector EXEC_INTEGUTIL Remote Command Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-14-344
- **ZDI-CAN:** ZDI-CAN-2266
- **Date:** 2014-10-02
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Data Protector
- **Credit:** Aniway.Anyway@gmail.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-344/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard Data Protector. Authentication is not required to exploit this vulnerability. The specific flaw exists within specifically crafted EXEC_INTEGUTIL messages. A remote attacker can inject arbitrary commands under the context of the SYSTEM user.

## Additional Details

This vulnerability is being disclosed publicly without a patch because vendor indicates that the vulnerability does not meet the bar for servicing. 04/16/2014 - ZDI disclosed to vendor 04/16/2014 - Vendor acknowledged and provided a tracking number 05/30/2014 - Vendor reported 'no fix' and workaround/mitigation -- Vendor Mitigation: You can enable the encrypted control communication from the command line as root by doing the below. Please review your configuration and enable it from the command line interface, executing: # omnicc -encryption -enable You can read up on the capability on page 145 of the User Guide. That guide is a PDF file, and found in /opt/omni/doc/C

## Disclosure Timeline

- 2014-04-16 - Vulnerability reported to vendor
- 2014-10-02 - Coordinated public release of advisory
