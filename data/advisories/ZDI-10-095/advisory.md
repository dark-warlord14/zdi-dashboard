# ZDI-10-095: Apple Webkit DOCUMENT_POSITION_DISCONNECTED Attribute Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-10-095
- **ZDI-CAN:** ZDI-CAN-632
- **Date:** 2010-06-08
- **CVE:** CVE-2010-1397
- **CVSS:** 10.0
- **CVSS Vector:** AV:N/AC:L/Au:N/C:C/I:C/A:C
- **Affected Vendors:** Apple
- **Affected Products:** WebKit
- **Credit:** wushi&Z of team509
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-10-095/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on software utilizing a vulnerable version of Apple's Webkit. User interaction is required to exploit this vulnerability in that the target must visit a malicious page. The specific flaw exists within the way that Apple's Webkit handles the DOCUMENT_POSITION_DISCONNECTED attribute when a container is removed. This attribute is responsible for ensuring that a node is disconnected from it's container and is implementation specific regarding the order of each node. If the disconnected element is removed from a particular type of container, the next time the application attempts to reference that container, the application will access memory that has been free which can lead to code execution under the context of the application.

## Additional Details

Apple has issued an update to correct this vulnerability. More details can be found at: http://support.apple.com/kb/HT4196

## Disclosure Timeline

- 2009-12-04 - Vulnerability reported to vendor
- 2010-06-08 - Coordinated public release of advisory
