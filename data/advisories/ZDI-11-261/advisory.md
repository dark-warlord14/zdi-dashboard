# ZDI-11-261: HP Easy Printer Care XMLSimpleAccessor Class ActiveX Control Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-11-261
- **ZDI-CAN:** ZDI-CAN-1092
- **Date:** 2011-08-16
- **CVE:** CVE-2011-2404
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Hewlett-Packard
- **Affected Products:** Easy Printer Care
- **Credit:** Andrea Micalizzi aka rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-11-261/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of HP Easy Printer Care. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the XMLSimpleAccessor class ActiveX control (CLSID 466576F3-19B6-4FF1-BD48-3E0E1BFB96E9). The SaveXML() method is vulnerable to directory traversal, which allows an attacker to write arbitrary content to the filesystem. A remote attacker could leverage this vulnerability to gain code execution under the context of the web browser.

## Additional Details

Title: c02949847 8/8/2011 Printing and Imaging HPSBPI02698 SSRT100404 rev.1 - HP Easy Printer Care Software Running on Windows, Remote Execution of Arbitrary Code URL (requires login) https://h20566.www2.hp.com/portal/site/hpsc/public/kb/docDisplay/?docId=emr_ na-c02949847 This URL will be available sometime in the future, if you need to use a no login required link. URL (no login required): http://h20000.www2.hp.com/bizsupport/TechSupport/Document.jsp?objectID=c0294 9847

## Disclosure Timeline

- 2011-02-17 - Vulnerability reported to vendor
- 2011-08-16 - Coordinated public release of advisory
