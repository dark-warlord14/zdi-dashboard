# ZDI-14-345: (0Day) Hewlett-Packard Data Protector omnidlc Buffer Overflow Remote Code Execution Vulnerabililty

## Metadata

- **ZDI ID:** ZDI-14-345
- **ZDI-CAN:** ZDI-CAN-2200
- **Date:** 2014-10-02
- **CVE:** N/A
- **CVSS:** 5.1
- **CVSS Vector:** AV:N/AC:H/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Data Protector
- **Credit:** Aniway.Anyway@gmail.com
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-14-345/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Hewlett-Packard Data Protector. Authentication is not required to exploit this vulnerability. The specific flaw exists within omnidlc.exe which can be called via crs.exe. The issue lies in the failure to properly validate the size of a string before copying it into a fixed-sized buffer. A remote attacker can chain this with another vulnerability to execute remote code under the context of the user running Data Protector.

## Additional Details

This vulnerability is being disclosed publicly without a patch because vendor indicates that the vulnerability does not meet the bar for servicing. 03/26/2014 - ZDI disclosed to vendor 03/26/2014 - Vendor acknowledged and provided a tracking number 05/30/2014 - Vendor reported 'no fix' and workaround/mitigation Mitigation: You can enable the encrypted control communication from the command line as root by doing the below. Please review your configuration and enable it from the command line interface, executing: # omnicc -encryption -enable You can read up on the capability on page 145 of the User Guide. That guide is a PDF file, and found in /opt/omni/doc/C

## Disclosure Timeline

- 2014-03-26 - Vulnerability reported to vendor
- 2014-10-02 - Coordinated public release of advisory
