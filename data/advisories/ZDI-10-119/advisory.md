# ZDI-10-119: Oracle Secure Backup Administration $other Variable Command Injection Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-119
- **ZDI-CAN:** ZDI-CAN-584
- **Date:** 2010-07-13
- **CVE:** CVE-2010-0899
- **CVSS:** 9.0
- **CVSS Vector:** AV:N/AC:L/Au:S/C:C/I:C/A:C
- **Affected Vendors:** Oracle
- **Affected Products:** Secure Backup
- **Credit:** Anonymous
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-119/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary commands on vulnerable installations of Oracle Secure Backup. Authentication is required to exploit this vulnerability. The specific flaw exists in the handling of variables to the property_box.php script located on the Oracle Secure Backup administration server. Due to the lack of filtering on special characters it is possible to specify arbitrary commands to the command line being executed by the administration server. Successful exploitation of this can lead to remote compromise under the credentials of the web server.

## Additional Details

Oracle has issued an update to correct this vulnerability. More details can be found at: http://www.oracle.com/technology/deploy/security/critical-patch-updates/cpujul2010.html

## Disclosure Timeline

- 2009-10-21 - Vulnerability reported to vendor
- 2010-07-13 - Coordinated public release of advisory
