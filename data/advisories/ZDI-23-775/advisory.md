# ZDI-23-775: (Pwn2Own) Unified Automation UaGateway OPC UA Server Improper Input Validation Denial-of-Service Vulnerability

## Metadata

- **ZDI ID:** ZDI-23-775
- **ZDI-CAN:** ZDI-CAN-20494
- **Date:** 2023-05-31
- **CVE:** CVE-2023-32170
- **CVSS:** 6.5
- **CVSS Vector:** AV:N/AC:L/PR:N/UI:R/S:U/C:N/I:N/A:H
- **Affected Vendors:** Unified Automation
- **Affected Products:** UaGateway
- **Credit:** Đỗ Minh Tuấn (@tuanit96) and Tran Van Khang (@khangkito) of STAR Labs SG Pte. Ltd.
- **Source:** https://www.zerodayinitiative.com/advisories/ZDI-23-775/
## Vulnerability Details

This vulnerability allows remote attackers to create a denial-of-service condition on affected installations of Unified Automation UaGateway. User interaction is required to exploit this vulnerability in that the target must choose to accept a client certificate. The specific flaw exists within the processing of client certificates. The issue results from the lack of proper validation of certificate data. An attacker can leverage this vulnerability to create a denial-of-service condition on the system.

## Additional Details

Unified Automation has issued an update to correct this vulnerability. More details can be found at: https://documentation.unified-automation.com/uagateway/1.5.14/CHANGELOG.txt

## Disclosure Timeline

- 2023-02-22 - Vulnerability reported to vendor
- 2023-05-31 - Coordinated public release of advisory
