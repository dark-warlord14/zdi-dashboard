# ZDI-11-272: (0Day) FlexNet License Server Manager Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-272
- **ZDI-CAN:** ZDI-CAN-1050
- **Date:** 2011-08-17
- **CVE:** N/A
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Flexera Software
- **Affected Products:** FlexNet License Server Manager
- **Credit:** Luigi Auriemma
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-272/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Flexnet License Server. Authentication is not required to exploit this vulnerability. The specific flaw exists within the license server manager which listens on TCP port 27000. There are multiple problems that allow an attacker to influence the saving and loading of log files on the server. By utilizing a directory traversal issue and some file renaming bugs, an attacker can leverage these vulnerabilities would allow the attacker to execute arbitrary code under the user context running the license server manager/vendor daemon.

## Additional Details

[August 17, 2011] - This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 180 day deadline. Mitigation supplied by vendor: Flexera Software takes security seriously and appreciates ZDIs efforts. Users of lmgrd, lmadmin and vendor daemons can virtually eliminate potential vulnerability by running the lmgrd, vendor daemon and lmadmin in the least privilege account possible. As a precautionary measure, Flexera Software will provide hotfix of the vendor daemon on various platforms starting in September. For more information and other tips to mitigate this potential vulnerability please see http://www.flexerasoftware.com/pl/13057.htm

## Disclosure Timeline

- 2011-02-17 - Vulnerability reported to vendor
- 2011-08-17 - Coordinated public release of advisory
