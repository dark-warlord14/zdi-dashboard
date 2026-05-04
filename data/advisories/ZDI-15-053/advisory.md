# ZDI-15-053: (0Day) Agilent Technologies Feature Extraction ActiveX Control Index Out-Of-Bounds Remote Code Execution Vulnerability

## Metadata

- **ZDI ID:** ZDI-15-053
- **ZDI-CAN:** ZDI-CAN-2288
- **Date:** 2015-02-27
- **CVE:** CVE-2015-2092
- **CVSS:** 7.5
- **CVSS Vector:** AV:N/AC:L/Au:N/C:P/I:P/A:P
- **Affected Vendors:** Agilent Technologies
- **Affected Products:** Feature Extraction
- **Credit:** rgod
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-15-053/
## Vulnerability Details

This vulnerability allows remote attackers to execute arbitrary code on vulnerable installations of Agilent Technologies Feature Extraction. User interaction is required to exploit this vulnerability in that the target must visit a malicious page or open a malicious file. The specific flaw exists within the AnnotationX.AnnList.1 ActiveX control included with the software. An attacker can use an unvalidated object parameter in the Insert() function to execute arbitrary code in the context of the browser.

## Additional Details

This vulnerability is being disclosed publicly without a patch in accordance with the ZDI 120 day deadline. 05/05/2014 - ZDI request for vulnerability contact with vendor 05/05/2014 - ZDI received reply and case # from the vendor 05/08/2014 - ZDI report sent to vendor 05/16/2014 - The vendor "acknowledged this defect" 12/02/2014 - ZDI requested any available update or ETA 12/05/2014 - The vendor replied "still pending" and no ETA 01/13/2015 - ZDI requested any available update or ETA 01/15/2015 - The vendor replied "still pending" and no ETA 02/13/2015 - ZDI notified of intent to 0-day 02/27/2015 - Public release of advisory 07/07/2015 - Vendor provided response -- Mitigation: The killbit can be set on this control to disable scripting within Internet Explorer by modifying the data value of the Compatibility Flags DWORD within the following location in the registry: HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Internet Explorer\ActiveX Compatibility\EF600D71-358F-11D1-8FD4-00AA00BD091C If the Compatibility Flags value is set to 0x00000400, the control can no longer be instantiated inside the browser. For more information, please see: http://support.microsoft.com/kb/240797 -- Vendor Response: Agilent recently released a software patch with Windows installers to address exposure to potential execution of the arbitrary code associated with Internet Explorer while ActiveX is activated. All Feature Extraction users (Version 12 or older) are strongly encouraged to execute the fix described below for protection against a potential malicious web page visited with Internet Explorer. http://www.genomics.agilent.com/article.jsp?pageId=4500002

## Disclosure Timeline

- 2014-05-05 - Vulnerability reported to vendor
- 2015-02-27 - Coordinated public release of advisory
